from bs4 import BeautifulSoup

soup = BeautifulSoup(open("form1.xml"),"html5lib")

f = open('view2.html', 'w')

tag=soup.panel
if soup.find("form") is not None: soup.form.unwrap()   #delete <form>

def func_panel(tag):
    tag.name="div"
    tag['id']=tag['name']
    del tag['name']
    if soup.find(id=tag['id']).find("height") is not None: del tag['height']

def func_lookup(tag):
    tag.name = "ui-select"
    tag['id'] = tag['name']
    del tag['name']
    if soup.find(id=tag['id']).find("label") is not None:
        tag['title'] = tag['label']
        del tag['label']
    if soup.find(id=tag['id']).find("data") is not None: del tag['data']

def func_label(tag):
    tag.name = "p"
    tag['id'] = tag['name']
    del tag['name']
    if soup.find(id=tag['id']).find("caption") is not None:
        tag.string = tag['caption']
        del tag['caption']

def func_grid(tag):
    tag.name= "div"
    tag['id'] = tag['name']
    del tag['name']
    tag['ui-grid'] = 'curr_grdOptions'
    tag['style'] = 'height: 450px;'


def func_column(tag):
    tag.name = "div-column"

def func_tabs(tag):
    tag.name = "uib-tabset"
    tag['justified'] = 'true'
    tag['id'] = tag['name']
    del tag['name']

def func_tab(tag):
    tag.name = "uib-tab"
    tag['id'] = tag['name']
    del tag['name']
    if soup.find(id=tag['id']).find("label") is not None:
        tag['heading'] = tag['label']
        del tag['label']

def func_button(tag):
    tag['id'] = tag['name']
    del tag['name']
    tag['type'] = 'button'
    tag['class'] = "btn btn-primary"
    if soup.find(id=tag['id']).find("caption") is not None:
        tag.string = tag['caption']
        del tag['caption']
    
def func_btn_group(tag):
    tag.name = "div"
    tag['class'] = "btn-group"

dict_func = {'panel': func_panel,
             'lookup': func_lookup,
             'label': func_label,
             'grid': func_grid,
             'column': func_column,
             'tabs': func_tabs,
             'tab': func_tab,
             'button': func_button,
             'btn_group': func_btn_group
            }
while tag is not None:
    if tag.name is not None:
            try:
                dict_func[tag.name](tag)
            except KeyError:
                print('Unknown tag name ' + tag.name)
    tag=tag.next


f.write(str(soup.prettify())) #formatter="html"
