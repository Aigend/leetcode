# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : BM23 二叉树的前序遍历.py
# @Date    : 2022/07/13:23:10
# @Author  : jinwenlong@oppo.com
"""
描述
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

数据范围：二叉树的节点数量满足 0 \le n \le 100 \0≤n≤100  ，二叉树节点的值满足 1 \le val \le 100 \1≤val≤100  ，树的各节点的值各不相同
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return int整型一维数组
#


from typing import List


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # write code here
        result = []
        if not root:
            return result
        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        return result


