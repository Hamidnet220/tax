class ViewGenerator():
    
    def __init__(self,table,entities=None,opration_buttons={},select_checkbox=False,add_url='',ordering=()):
        self.table=table
        self.entites=entities
        self.add_url=add_url
        self.select_checkbox=select_checkbox
        self.opration_buttons=opration_buttons
        self.ordering=ordering
    # get all fields names of table 
    def get_filed_names(self):
        filed_names=list()
        for f in self.table._meta.get_fields():
            if hasattr(f,'verbose_name') and f.name!='id':
                filed_names.append(f.name)
        return filed_names
        
    # get all fields labels of table
    def get_field_labels(self):
        field_labels=list()
        field_labels.append('ردیف')
        for f in self.table._meta.get_fields():
            if hasattr(f,'verbose_name') and f.name!='id':
                field_labels.append(f.verbose_name)
        return field_labels

    # create context for html template
    def get_context_template(self,id=''):
        if self.entites is None:
            if id!="":
                objects=self.table.objects.all().filter(id=id).order_by(*(self.ordering))
            else:
                objects=self.table.objects.all().filter().order_by(*(self.ordering))
        else:
            objects=self.entites

        context={
        'objects':objects,
        'titles': self.get_field_labels(),
        'field_names':self.get_filed_names(),
        'add_url_name':self.add_url,
        'opration_buttons':self.opration_buttons,
        'select_checkbox':self.select_checkbox,
        
        }

        return context


   