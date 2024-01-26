db.createCollection("sensor", {
    validator: {
       $jsonSchema: {
          bsonType: "object",
          required: [ "time","temperature","humidity","lux","distance" ],
          properties: {
             time: {
                bsonType: "int",
                description: "integer unixtime: required"
             },
             temperature: {
                bsonType: "int",
                description: "integer Celcius Degrees: required"
             },
             humidity: {
                bsonType: "int",
                description: "integer RH%: required"
             },
             lux: {
               bsonType: "float",
               description: "float lux: required"
             },
             distance: {
               bsonType: "float",
               description: "float cm: required"
             }
            
          }
       }
    }
 })