# JSONのdumpsとloadsの実装

Python dictからJSON Stringへの変換を行うdumps、JSON StringからPython dictへの変換を行うloadsを実装。


Valueの型は、int, float, str, dict, listに対応。


	現在は、多次元配列など括弧が二重以上になる場合のloadsができない状態。

	[1, 2, 3]は扱えるが
	[[1, 2, 3], [4, 5, 6]]などはエラーが発生する。→正規表現の関係で、[[1, 2, 3]となる。