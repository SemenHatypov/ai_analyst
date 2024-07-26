import os

import yaml


# Function to generate YAML file for a given table
def generate_yaml(table_name, description, fields):
    # Define the directory path where YAML files will be stored
    data_dir = "data/" + table_name
    # Create the directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)

    # Define the structure of the YAML data
    yaml_data = {"table_name": table_name, "description": description, "fields": fields}

    # Define the file path for the YAML file
    yaml_file = os.path.join(data_dir, f"{table_name}.yml")

    # Write the YAML data to the file
    with open(yaml_file, "w") as file:
        yaml.safe_dump(yaml_data, file)

    # Print a message indicating the YAML file creation
    print(f"Generated YAML file for {table_name}: {yaml_file}")


# Main function to generate YAML files for each table
if __name__ == "__main__":
    # Define the structure for the 'session' table
    session_description = "Table for storing user sessions"
    session_fields = [
        {
            "description": "Unique identifier of the session",
            "name": "id",
            "type": "integer",
        },
        {
            "description": "Time of session",
            "name": "session_timestamp",
            "type": "timestamp",
        },
        {
            "description": "Unique identifier of the user",
            "name": "user_id",
            "type": "integer",
        },
        {
            "description": "User location",
            "name": "user_location",
            "type": "string",
        },
        {
            "description": "User device (web/ios/android etc)",
            "name": "user_device",
            "type": "string",
        },
    ]
    # Generate YAML file for 'session' table
    generate_yaml("session", session_description, session_fields)

    # Define the structure for the 'search' table
    search_description = (
        "Table for storing user search of destination during the session"
    )
    search_fields = [
        {
            "description": "Unique identifier of the search",
            "name": "id",
            "type": "integer",
        },
        {
            "description": "Identifier of the related session",
            "name": "session_id",
            "type": "integer",
        },
        {
            "description": "Time of search",
            "name": "search_timestamp",
            "type": "timestamp",
        },
        {
            "description": "Name of the city user searched",
            "name": "destination_city",
            "type": "string",
        },
        {
            "description": "First date of the trip (optional)",
            "name": "first_date",
            "type": "date",
        },
        {
            "description": "Last date of the trip (optional)",
            "name": "last_date",
            "type": "date",
        },
    ]
    # Generate YAML file for 'search' table
    generate_yaml("search", search_description, search_fields)

    # Define the structure for the 'open_activity' table
    open_activity_description = (
        "Table for storing opened activities from search results"
    )
    open_activity_fields = [
        {
            "description": "Unique identifier of opening the activity",
            "name": "id",
            "type": "integer",
        },
        {
            "description": "Identifier of the related search",
            "name": "search_id",
            "type": "integer",
        },
        {
            "description": "Identifier of the activity",
            "name": "activity_id",
            "type": "integer",
        },
        {
            "description": "Type of the activity",
            "name": "activity_type",
            "type": "string",
        },
        {
            "description": "Time of the opening the activity",
            "name": "open_activity_timestamp",
            "type": "timestamp",
        },
        {
            "description": "Showed price in USD",
            "name": "showed_price",
            "type": "decimal",
        },
    ]
    # Generate YAML file for 'open_activity' table
    generate_yaml("open_activity", open_activity_description, open_activity_fields)

    # Define the structure for the 'purchase' table
    purchase_description = "Table for storing purchaseed activities"
    purchase_fields = [
        {
            "description": "Unique identifier of purchase",
            "name": "id",
            "type": "integer",
        },
        {
            "description": "Identifier of the related opening the activity",
            "name": "open_activity_id",
            "type": "integer",
        },
        {
            "description": "Date of booked activity",
            "name": "activity_date",
            "type": "date",
        },
        {
            "description": "Amount of clients booked an activity",
            "name": "clients_count",
            "type": "integer",
        },
        {
            "description": "Paid price in USD",
            "name": "paid_price",
            "type": "decimal",
        },
        {
            "description": "Commission of service in USD",
            "name": "commision",
            "type": "decimal",
        },
        {
            "description": "Time of the opening the activity",
            "name": "open_activity_timestamp",
            "type": "timestamp",
        },
    ]
    # Generate YAML file for 'purchase' table
    generate_yaml("purchase", purchase_description, purchase_fields)
