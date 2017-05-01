truck_schema = {
	"type" : "object",
	"properties" : {
		"truck_model" : {
			"type": "string"
		},
		"max_weight": {
			"type": "number",
			"minimum": 0,
			"exclusiveMinimum": True
		},
		"max_volume": {
			"type": "number",
			"minimum": 0,
			"exclusiveMinimum": True
		}
	},
	"required": ['truck_model', "max_volume", "max_weight"]
}

booking_schema = {
	"type": "object",
	"properties": {
		
		"source": {
			"type": "string"
		},
		"destination": {
			"type": "string"
		},
		"item_desc": {
			"type": "string"
		},
		"weight": {
			"type": "number",
			"minimum": 0,
			"exclusiveMinimum": True
		},
		"volume": {
			"type": "number",
			"minimum": 0,
			"exclusiveMinimum": True
		},
		"start_date": {
			"type": "datetime"
		},
		"end_date": {
			"type": "datetime"
		}
	},
	"required": ["source", "destination", "item_desc", "weight", "volume", "start_date", "end_date"]
}

truck_location_schema = {
	"type": "object",
	"properties": {
		"truck_id": "number"
	},
	"required": ["truck_id"]
}