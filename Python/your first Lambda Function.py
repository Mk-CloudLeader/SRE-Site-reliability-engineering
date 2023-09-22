# Create function Author from scratch "Start with a simple Hello World example."

import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


# The only real difference in the code, is that now we're going to dump the event object into the body of the return object, 
# rather than just a static string of "Hello from Lambda"

import json
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
