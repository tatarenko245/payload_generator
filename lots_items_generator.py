import json
from uuid import uuid4
import random

status = ['active', 'complete', 'cancelled']
statusDetails = ['empty']

lot_id = uuid4()
item_id = uuid4()

schema_lot = {
    "id": str(lot_id),
    "title": "My tea's gone cold I'm wondering why I got out of bed at all ",
    "description": "The morning rain clouds up my window",
    "status": str(random.choice(status)),
    "statusDetails": str(random.choice(statusDetails)),
    "value": {
        "amount": 10.00,
        "currency": "EUR"
    },
    "options": [{
        "hasOptions": False
    }],
    "variants": [{
        "hasVariants": False
    }],
    "renewals": [{
        "hasRenewals": False
    }],
    "recurrentProcurement": [{
        "isRecurrent": False
    }],
    "contractPeriod": {
        "startDate": "2020-04-28T14:45:00Z",
        "endDate": "2020-04-30T14:45:00Z"
    },
    "placeOfPerformance": {
        "address": {
            "streetAddress": "6666",
            "postalCode": "666",
            "addressDetails": {
                "country": {
                    "scheme": "iso-alpha2",
                    "id": "MD",
                    "description": "MOLDOVA",
                    "uri": "http://reference.iatistandard.org"
                },
                "region": {
                    "scheme": "CUATM",
                    "id": "1000000",
                    "description": "Anenii Noi",
                    "uri": "http://statistica.md"
                },
                "locality": {
                    "scheme": "666",
                    "id": "666",
                    "description": "666"
                }
            }
        },
        "description": "And I can't see at all"
    }
}

schema_item = {
    "id": str(item_id),
    "internalId": "item 1",
    "classification": {
        "id": "50100000-6",
        "scheme": "CPV",
        "description": "description"
    },
    "additionalClassifications": [{
        "id": "AA12-4",
        "scheme": "CPVS",
        "description": "description"
    }],
    "quantity": 0.01,
    "unit": {
        "id": "10",
        "name": "name"
    },
    "description": "description",
    "relatedLot": str(lot_id)
}


# ВНимание! В переменную "quantity" нужно указать количество объектов, которые необходимы в массиве lots и items.
# После вывода результата нужно поправить  json, а именно убрать "{" вначале и "}" вконце.
quantity = 2

lots = [schema_lot for _ in range(quantity)]
items = [schema_item for _ in range(quantity)]

schema_lots_item = {
    "lots": lots,
    "items": items
}
print(json.dumps(schema_lots_item, indent=4))

