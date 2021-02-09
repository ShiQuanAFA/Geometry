#!/usr/bin/env python3
# -*- coding: utf-8 -*-
{
FrozenMultiset({FrozenMultiset({'b'}): 1, FrozenMultiset({'c'}): 1}): 1
}=={
FrozenMultiset({FrozenMultiset({'c'}): 1, FrozenMultiset({'b'}): 1}): 1
}

{
frozenset({
frozenset({frozenset({'b'}), frozenset({'c'})})
})}=={
frozenset({
frozenset({frozenset({'c'}), frozenset({'b'})})
})
}

{
FrozenMultiset([frozenset({'b'}) , frozenset({'a'})])
} == {
FrozenMultiset([frozenset({'a'}) , frozenset({'b'})])
}

# value equal
{
FrozenMultiset([frozenset({'b'}) , frozenset({'a'})])
} == {
FrozenMultiset([frozenset({'a'}) , frozenset({'b'})])
}
# deep equal
{
FrozenMultiset(['b' , 'a'])
} == {
FrozenMultiset(['a' , 'b'])
}
# value equal
FrozenMultiset(
FrozenMultiset(['b' , 'a'])
) == FrozenMultiset(
FrozenMultiset(['a' , 'b'])
)

{
FrozenMultiset([('segment', 'BM'), ('segment', 'ME')])
} == {
FrozenMultiset([('segment', 'ME'), ('segment', 'BM')])
}

{
FrozenMultiset({
FrozenMultiset([('segment', 'BM'), ('segment', 'ME')])
})
} == {
FrozenMultiset({
FrozenMultiset([('segment', 'ME'), ('segment', 'BM')])
})
}
