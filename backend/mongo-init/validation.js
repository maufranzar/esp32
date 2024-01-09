db.createCollection("sensor", {
    validator: {
       $jsonSchema: {
          bsonType: "object",
          required: [ "time", "temperature", "humidity", "lux" ],
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
            }
          }
       }
    }
 })