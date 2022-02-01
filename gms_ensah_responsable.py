from osv import osv,fields
# import openerp


class gms_ensah_responsable(osv.osv):
    _name= 'gms.ensah.responsable'
    _columns={
        'image':fields.binary('Image', filters="*.png"),
        'name':fields.char('Nom Complet', required=True) ,
        'phone':fields.char('Telephone', required=True)  ,
        'email': fields.char('Email', required=True) ,
        'status': fields.char('Status', required=True),
        'id_manifes':fields.many2one('gms.ensah.manifestation','Manifestation', ondelete='cascade'),

    }

gms_ensah_responsable()