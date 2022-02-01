from osv import osv,fields
# import openerp


class gms_ensah_participant(osv.osv):
    _name= 'gms.ensah.participant'
    _columns={
        'image':fields.binary('photo_participant', filters="*.png"),
        'name':fields.char('Nom Complet', required=True) ,
        'CNE':fields.char('CNE', required=True)  ,
        'phone':fields.char('Number')  ,
        'email': fields.char('Email', required=True) ,
        'age': fields.integer('Age', required=True) ,
        'residence': fields.boolean('Residence') ,
        'date_naissance': fields.date('Date de naissance') ,
        'address': fields.char('Address', required=True) ,
        'id_manifestation':fields.many2one('gms.ensah.manifestation','Manifestation', ondelete='cascade'),
    } 
    def create(self,cr,uid,values,context=None):
        print(values)
        if values["id_manifestation"]:
            ManifestModel=self.pool.get("gms.ensah.manifestation")
            obj=ManifestModel.browse(cr,uid,values["id_manifestation"],context=context)
            print(obj)
            ManifestModel.write(cr,uid,[values["id_manifestation"]],{'n_participant':(int(obj.n_participant)+1)})
        return super(gms_ensah_participant,self).create(cr,uid,values,context=context)
gms_ensah_participant()