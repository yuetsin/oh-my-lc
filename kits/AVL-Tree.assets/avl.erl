balance(null) -> null;
balance({null, _, null}=Tree) -> Tree;
balance({Left, Value, Right}=Tree) ->
    Diff = count(Left)-count(Right)
    if (Diff < 2) and (Diff > -2) -> {balance(Left), Value, balance(Right)};
                       (Diff > 1) -> balance(rotate_right(Tree));
                      (Diff < -1) -> balance(rotate_left(Tree));
                             true -> exit('This is impossible!')
    end.

rotate_right({Left, Value, Right}) ->
    merge_max(Left, {null, Value, Right}).

rotate_left({Left, Value, Right}) ->
    merge_min(Right, {Left, Value, null}).

merge_min({null, Value, Right}, Tree2) ->
    {Tree2, Value, Right};

merge_min({Left, _, _}, Tree2) ->
    merge_min(Left, Tree2).

merge_max({Left, Value, null}, Tree2) ->
    {Left, Value, Tree2};

merge_max({_, _, Right}, Tree2) ->
    merge_max(Right, Tree2).