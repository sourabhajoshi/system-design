from vehical import Vehical
import json

class ObjectFormatter:
    def vehical_to_json(self, vehical:Vehical):
        return json.dumps({
            "VehicalMake" : vehical.make,
            "VehicalModel" : vehical.model,
            "VehicalYear" : vehical.year
        })