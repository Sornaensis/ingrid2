Theorem Specification Language for Ingrid 2
------------------------------

* Users can input their own theorems into Ingrid 2 using this purpose built language
* Capable of expressing almost all necessary components of a theorem
* High degree of automatic boundary analysis


Basic Concepts
--------------

At their heart, most theorems, or class constraints, are expressed as inequalities such as the following.

```
edgeChromatic <= 2*bandwidth;
```

For inequalities, the TSL compiler automatically applies boundary analysis and term rewriting, resulting in the following expression.

```
edgeChromatic <= 2.0*maxb(bandwidth);
bandwidth >= minb(edgeChromatic)/2.0;
```

These inequalities do not contain any `free invariants`, or invariants that are not surrounded by either the `minb()` or maxb()` functions, so they are considered final.

Conditional expressions are also permitted.

```
if diameter <= 2 then
{
    edgeConnec = mindeg
};
```

The symbols `=` and `==` are treated identically by the compiler for convenience.

The above program turns into the following expression after analysis.

```
if maxb(diameter) <= 2.0 then 
{
    edgeConnec >= minb(mindeg),
    mindeg <= maxb(edgeConnec),
    edgeConnec <= maxb(mindeg),
    mindeg >= minb(edgeConnec)
};
```

Each invariant boundary is automatically checked for 'indeterminacy', which is handled symbolically within the Ingrid 2 constraint solver, so expressions dealing with infinity are avoided, and boundaries may be initially set to arbitrarily large sizes for maximum boundaries.

Finally, the language also allows for both imperative, mutable variables, and immutable symbolic bindings.

Mutable variables must begin with an underscore (_) and have special syntax for assigning values:

`\_mut is <expr>`

```
if nodeConnec >= 2 then
{
    _minpd is minimum(nodes, 2*mindeg);
} 
else
{
    _minpd is 6,
};
circumference >= _minpd;
```

The value stored in `\_minpd` behaves as you would expect in a C or pascal program.


Symbolic variables are assigned with the `let` statement, and are symbolically replaced by their RHS expression before any term re-writing or analysis is done.

So the theorem

```
let r = 2*nodes-edges;
numOfComponents <= r;
spectralRadius <= sqrt(r);
```

Becomes

```
numofComponents <= 2.0*maxb(nodes)-(minb(edges));
nodes >= minb(edges)/2.0+minb(numofComponents)/2.0;
edges <= 2.0*maxb(nodes)-(minb(numofComponents));
spectralRadius <= sqrt(2.0*maxb(nodes)-(minb(edges)));
nodes >= minb(edges)/2.0+minb(spectralRadius)**2.0/2.0;
edges <= 2.0*maxb(nodes)-(minb(spectralRadius)**2.0);
```

After all terms have been re-written and had analysis applied to them.

Structure
---------

Each theorem 'program' is a sequence of assertions under conjunction.

The basic syntax is as follows:

```
<statement>;
<statement>;
...
<statement>;
if <condition> then
{
    <statement>,
    ...
    <statement>,
    if <condition> then
    {
        ...
    },
    <statement>
} 
else if <condition> then
{
    <statement>,
    ...
    <statement>,
    if <condition> then
    {
        ...
    },
    <statement>
}
else
{
    <statement>,
    ...
    <statement>,
    if <condition> then
    {
        ...
    },
    <statement>
};
```


* Statements are asserted in the order they are specified, from top to bottom.
* If statement bodies contain lists of statements which are comma-separated, and can contain nested if-statements.
* An entire `if else-if else` block is considered one large statement that only has a semicolon or comma at the end.
* Let statements may not reside within if statements.
