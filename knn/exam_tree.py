# encode:utf-8
from anytree import Node, RenderTree

udo = Node("Udo")
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
for pre, fill, node in RenderTree(udo):
    print("%s%s" % (pre, node.name))
