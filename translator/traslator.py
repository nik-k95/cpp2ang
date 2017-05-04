from bs4 import BeautifulSoup

soup = BeautifulSoup(open("form1.xml"),"html5lib")

f = open('view2.html', 'w')

soup.form.unwrap()
#panel1
tag=soup.panel
tag.name = "div"
tag['class'] = 'row'
tag['style']='margin-left: 5px; margin-right: 5px'
tag['id']=tag['name']
del tag['name']
del tag['height']
new_tag = soup.new_tag("div") #bootstrap
tag.insert(1,new_tag)
new_tag['class'] = "col-lg-12"
tag=new_tag
new_tag = soup.new_tag("div")
new_tag['class'] = "panel panel-default"
tag.insert(1,new_tag)

tag=new_tag
new_tag = soup.new_tag("div")  #bootstrap
tag.insert(1,new_tag)
new_tag['class'] = "col-lg-1 col-sm-1"
tag=new_tag
new_tag = soup.new_tag("div")
tag.wrap(new_tag)
new_tag['class'] = "panel-body"
tag=new_tag
new_tag = soup.new_tag("div")
tag.insert(1,new_tag)
new_tag['class'] = "col-lg-8 col-sm-8"

#lookup
tag=soup.lookup
tag.name="ui-select"
tag['id']=tag['name']
del tag['name']
tag['title']=tag['label']
del tag['label']
del tag['data']
tag['ng-model theme']='select2'
tag['ng-disabled']='false'
tag['style']='width:100%'
new_tag=tag.previous
new_tag.insert(1,tag)

new_tag = soup.new_tag("ui-select-match")
tag.append(new_tag)
new_tag.string = "{{$select.selected.NAME}}"
new_tag = soup.new_tag("ui-select-choices")
tag.append(new_tag)
new_tag['repeat'] = 'y in data_levels'
tag=new_tag
new_tag = soup.new_tag("div")
tag.append(new_tag)
new_tag['ng-bind-html'] = 'trustAsHtml(y.NAME)'



#main_panel
tag=soup.panel
tag.name = "div"
tag['class'] = 'row'
tag['style']='margin-left: 5px; margin-right: 5px'
tag['id']=tag['name']
del tag['name']
new_tag = soup.new_tag("div") #bootstrap
tag.insert(1,new_tag)
new_tag['class'] = "col-lg-7 col-sm-7 col-xs-7"

tag=new_tag
new_tag=soup.panel
new_tag.name="div"
new_tag['class'] = "panel panel-default"
new_tag['id']=new_tag['name']
del new_tag['name']
tag.insert(1,new_tag)
tag=new_tag
new_tag = soup.new_tag("div")
tag.insert(1,new_tag)
new_tag['class'] = "panel-body"
tag=new_tag
new_tag = soup.new_tag("p")
tag.insert(1,new_tag)
new_tag.string = "Учебные планы"
soup.label.decompose()
tag=new_tag
new_tag = soup.new_tag("div")
tag.insert_after(new_tag)
new_tag['id']='curr_grd'
new_tag['ui-grid']='curr_grdOptions'
new_tag['style']='height: 450px;'
new_tag['ui-grid-cellNav ui-grid-resize-columns ui-grid-move-columns ui-grid-pinning ui-grid-selection ui-grid-exporter ui-grid-auto-resize ng-click']='curr_grdClick()'
soup.grid.decompose()

#content_panel
tag=soup.panel
tag.name = "div"
tag['class'] = 'col-lg-5 col-sm-5 col-xs-5'
tag['id']=tag['name']
del tag['name']
tag=soup.tabs
tag.name = "uib-tabset"
tag['justified']='true'
tag['id']=tag['name']
del tag['name']
tag=soup.tab
tag.name = "uib-tab"
tag['heading']=tag['label']
tag['id']=tag['name']
del tag['name']
del tag['label']
tag=soup.panel
tag.name = "div"
tag['id']='grid2'
tag['ui-grid-cellNav ui-grid-resize-columns ui-grid-move-columns ui-grid-pinning ui-grid-selection ui-grid-exporter ui-grid-auto-resize ui-grid']='files_grdOptions'
del tag['name']
soup.button.decompose()
soup.column.decompose()
soup.grid.decompose()
soup.button.unwrap()
tag=soup.tab
tag.name = "uib-tab"
tag['heading']=tag['label']
tag['id']=tag['name']
del tag['name']
del tag['label']
new_tag = soup.new_tag("div")
tag.insert(1,new_tag)
new_tag['class'] = "row"
tag=new_tag
new_tag = soup.new_tag("div") #bootstrap
tag.insert(1,new_tag)
new_tag['class'] = "col-lg-12"
tag=soup.tabs
tag.name = "uib-tabset"
tag['justified']='true'
tag['id']='my_tabs2'
del tag['name']
tag=soup.tab
tag.name = "uib-tab"
tag['heading']=tag['label']
tag['id']=tag['name']
del tag['name']
del tag['label']
#btn-group
tag=soup.btn_group
tag.name="div"
tag['class'] = "btn-group"
new_tag=soup.button  #buttons
tag.insert(1,new_tag)
new_tag['type']='button'
new_tag['class'] = "btn btn-primary"
new_tag.string=new_tag['caption']
del new_tag['caption']
new_tag=soup.find("button",caption="Action2")
tag.insert(2,new_tag)
new_tag['type']='button'
new_tag['class'] = "btn btn-primary"
new_tag.string=new_tag['caption']
del new_tag['caption']
new_tag=soup.find("button",caption="Action3")
tag.insert(3,new_tag)
new_tag['type']='button'
new_tag['class'] = "btn btn-primary"
new_tag.string=new_tag['caption']
del new_tag['caption']
tag=soup.find("uib-tab",id="tb21")
new_tag = soup.new_tag("uib-tab")
tag.insert_after(new_tag)
new_tag['heading']='Small Button'
new_tag['id']='tb22'
new_tag=soup.find("uib-tabset",id="my_tabs2")
tag=new_tag.previous
tag.insert(1,new_tag)
new_tag=soup.find("uib-tab",id="tab2")
tag=soup.find("uib-tabset",id="my_tabs")
tag.insert(2,new_tag)

f.write(str(soup.prettify())) #formatter="html"

# import json
# form1.json= json.dumps(tree)
# print(form1)
