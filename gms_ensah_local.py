from osv import osv,fields
# import openerp


class gms_ensah_local(osv.osv):
    _name= 'gms.ensah.local'
    _columns={
        'name':fields.char('Labelle', required=True) ,
        'address':fields.char('Adress', required=True)  ,
        'id_man':fields.many2one('gms.ensah.manifestation','Manifestation', ondelete='cascade'),

    }

gms_ensah_local()