# concept for neuralmind
# i want to be able to open and save a file which saves a **mind**
# when it opens, it will show a web out of the central (mind) i.e. person
# upon selecting a category, it will devolve into nodes or other categories
# you can add as many categories and subcategories
# you can add as many nodes under any category
# the nodes can be text, images, checklists, tables, drawings (probably in order of implementation)
# can link nodes to other nodes (quick way, will search all nodes, and you can select. 
# the link will show up in the neural-network-style  and when opening a node, it will show a sidebar with all the linked nodes


def setup():
    size(1800,950)
    background(8,8,8)


def draw():
    if mousePressed:
        stroke(255,255,255)
    else:
        stroke(0,0,0)
    line(width/2,height/2,mouseX,mouseY)
    