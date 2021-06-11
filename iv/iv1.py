'''

二叉树 root  p q
'''


def nearestparents(root, p, q):
    res = None

    def helper(root):
        if not root: return False
        nonlocal res
        l = helper(root.left)

        r = helper(root.right)

        mid = root.val == p or root.val == q

        if l + r + mid >= 2:
            # found the target
            res = root
            return

        return l or r or mid

    helper(root)

    return res
