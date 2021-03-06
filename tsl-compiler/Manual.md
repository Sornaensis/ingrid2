Theorem Specification Language for Ingrid 2
==============================

* Users can input their own theorems into Ingrid 2 using this purpose built language
* Capable of expressing almost all necessary components of a theorem
* High degree of automatic boundary analysis


Basic Concepts
==============

At their heart, most theorems, or class constraints, are expressed as inequalities such as the following.

```haskell
edgeChromatic <= 2*bandwidth;
```

For inequalities, the TSL compiler automatically applies boundary analysis and term rewriting, resulting in the following expression.

```haskell
edgeChromatic <= 2.0*maxb(bandwidth);
bandwidth >= minb(edgeChromatic)/2.0;
```

These inequalities do not contain any `free invariants`, or invariants that are not surrounded by either the `minb()` or `maxb()` functions, so they are considered final.

We use `minb()` and `maxb()` to get the minimum and maximum bounds of a numerical invariant, respectively. 

For boolean invariants, there are only two methods for either asserting or de-asserting, or checking whether they are true or false:

```haskell
complete;
not planar;
```

The first statement asserts that `complete` must be true, the second that `planar` must be false.

Conditional expressions are also permitted.

```haskell
if diameter <= 2 then
{
    edgeConnec = mindeg
};
```

The symbols `=` and `==` are treated identically by the compiler for convenience.

The above program turns into the following after analysis.

```haskell
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

`_var is <expr>`

```haskell
if nodeConnec >= 2 then
{
    _minpd is minimum(minb(nodes), 2*minb(mindeg))
} 
else
{
    _minpd is 6
};
circumference >= _minpd;
```

The value stored in `_minpd` behaves as you would expect in a C or pascal program.


Symbolic variables are assigned with the `let` statement, and are symbolically replaced by their RHS expression before any term re-writing or analysis is done.

So the theorem

```haskell
let r = 2*nodes-edges;
numOfComponents <= r;
spectralRadius <= sqrt(r);
```

Becomes

```haskell
numofComponents <= 2.0*maxb(nodes)-(minb(edges));
nodes >= minb(edges)/2.0+minb(numofComponents)/2.0;
edges <= 2.0*maxb(nodes)-(minb(numofComponents));
spectralRadius <= sqrt(2.0*maxb(nodes)-(minb(edges)));
nodes >= minb(edges)/2.0+minb(spectralRadius)**2.0/2.0;
edges <= 2.0*maxb(nodes)-(minb(spectralRadius)**2.0);
```

After all terms have been re-written and had analysis applied to them.

Syntax
=========

Each theorem 'program' is a sequence of assertions under conjunction.

The basic syntax is as follows:

```haskell
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

* All statements must end with a semi colon unless within an if statement
* Statements are asserted in the order they are specified, from top to bottom.
* If statement bodies contain lists of statements which are comma-separated, and can contain nested if-statements.
* An entire `if else-if else` block is considered one large statement that only has a semicolon or comma at the end.
* Let statements may not reside within if statements.

For statements, only the following relational expressions are allowed:

```haskell
invar <= <expr>;
invar >= <expr>;
invar == <expr>;
```

For conditions (if statements), we allow `<` and `>` as well as `!=`.

Built In Functions
==================

`minimum(x,y)`

`maximum(x,y)`

`even(x)`

`odd(x)`

`not(x)`

`ceiling(x)`

`floor(x)`

`log(x,[y])`

`ln(x)`

`cos(x)`

`sin(x)`

`congruent(invar,x,y)`

`pi()`

`setmin(invar, x)*`

`setmax(invar, x)*`

`minb(invar)`

`maxb(invar)`

* Note: `invar` in the functions above indicates that the function must take an invariant as a parameter rather than an expression, while brackets [] indicate an optional argument
* Note: * indicates that the function may only be used as a statement, not within an expression, and not within a condition

Special Statements
============================

Even and Odd
------------

```haskell
even invar;
```

Meaning: 
* Assert that `invar` must have an even value

```haskell
odd invar;
```

Meaning:
* Asserts that `invar` must have an odd value

Isset
-----

```haskell
if isset invar then { ... };
```

Meaning: Checks whether `maxb(invar) == minb(invar)`

Existence or Definition
-----------------------

```haskell
undefined invar;
```

Meaning:
* Asserts that the invariant has both undetermined maximum and minimum boundaries

```haskell
if defined invar then { ... };
```

Meaning:
* Checks whether `invar` has a minimum bound less than infinity

```haskell
if exists invar then { ... };
```

Meaning:
* Checks whether `invar` has a maximum bound less than infinity

Boolean Assertion
-----------------

```haskell
invar;
```

Meaning:
* Asserts that `invar` has the value true, if `invar` is a boolean invariant. Otherwise error.

```haskell
not invar;
```

Meaning:
* Asserts that `invar` has the value false, if `invar` is a boolean invariant. Otherwise error.

Boolean Expressions
-------------------

Arbitrary boolean expressions cannot be inserted into conditions, they must be preceded by special directives:

```haskell
if istrue congruent(nodes, 3, 4) then { ... };
if istrue <expr> then { ... };
```

```haskell
if isfalse <expr> then { ... };
```

Meaning: `istrue` followed by an expression that resolves to a boolean value checks whether the expression is true,
`isfalse` checks whether it is false.

* Note: if the expression does not resolve to a boolean value the theorem will be skipped at runtime but this may not produce a compile time error!

Equation Solving
----------------

```haskell
nosolve invar <= <expr>;
```

Meaning:
* Does not solve `invar <= <expr>` for each term, but does apply analysis to free invariants.

```haskell
invar <= <expr> : useMinFor(invar2);
```

Meaning:
* When solving the expression for `invar2`, treat it as though the analysis concluded to use its minimum boundary

```haskell
invar >= <expr> : useMaxFor(invar2);
```

Meaning:
* When solving the expression for `invar2`, treat it as though the analysis concluded to use its maximum boundary.
