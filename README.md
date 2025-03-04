


# Phone Number Location Mapper

This project utilizes Python to map locations associated with phone numbers. It makes use of the `phonenumbers` library to extract information about the phone number, and the `OpenCage` geocoding service to get geographical coordinates corresponding to the phone number's location. Finally, it creates an interactive map using the `folium` library.

## Features

- Parse and validate phone numbers.
- Retrieve the geographic location, service provider, and time zone of a phone number.
- Map the location using `folium` and save it as an HTML file.

## Prerequisites

Make sure you have Python 3.6 or higher installed on your machine. You will also need to install the required libraries:

```bash
pip install phonenumbers folium opencage
```

## API Key

To use the OpenCage geocoding service, you need to sign up for an API key. Replace `add api key` in the code with your actual API key.

## Usage

1. **Set Up**: Ensure you have the required libraries installed and have replaced the placeholder text with your OpenCage API key in the code.

2. **Run the Script**: Save the provided code into a Python file (e.g., `phone_location_mapper.py`).

3. **Phone Number Input**: Update the variable `number` in the code with the phone number you wish to map (ensure it includes the correct formatting).

    Example:
    ```python
    number = "+1234567890" # Replace with the desired phone number
    ```

4. **Execute the Script**: Run the script using Python.

    ```bash
    python phone_location_mapper.py
    ```

5. **Output**: Upon successful execution, the script will create a file called `Location.html`, which you can open in a web browser to view the interactive map.

## Example Output

After running the script with a valid phone number and API key, you might see output like this:

```
Location: San Francisco, California
Service Provider: AT&T
Time Zone: ['America/Los_Angeles']
```

A map will be generated with a marker at the corresponding location.

## Notes

- Make sure the phone number is formatted correctly, including the country code.
- For larger-scale implementations, consider handling exceptions and errors, such as invalid phone number formats or issues with the API service.

## License

This project is open source and available under the MIT License. Feel free to modify and improve it.

## Contact

For any questions or feedback, please contact Harshavardhan SR at harshavardhanmywork@gmail.com.
```

You can replace `Harshavardhan SR` and `harshavardhanmywork@gmail.com` with your actual contact information. This format should be suitable for a GitHub repository.
