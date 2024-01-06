db.createCollection("sensor", {
    validator: {
       $jsonSchema: {
          bsonType: "object",
          required: [ "time", "temperature", "humidity" ],
          properties: {
             time: {
                bsonType: "int",
                description: "must be an integer and is required"
             },
             temperature: {
                bsonType: "int",
                description: "must be an integer and is required"
             },
             humidity: {
                bsonType: "int",
                description: "must be an integer and is required"
             }
          }
       }
    }
 })