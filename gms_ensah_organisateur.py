from osv import osv,fields
# import openerp


class gms_ensah_organisateur(osv.osv):
    _name= 'gms.ensah.organisateur'
    _columns={
        'image': fields.binary('photo_organisateur', filters="*.png"),
        'name':fields.char('Nom Complet', required=True) ,
        'phone':fields.char('Telephone', required=True)  ,
        'email': fields.char('email', required=True) ,
        'id_manifest':fields.many2one('gms.ensah.manifestation','Manifestation', ondelete='cascade'),

    }

gms_ensah_organisateur()