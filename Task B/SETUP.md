# Quick Setup Guide

## Prerequisites
- Ruby 3.0 or higher
- Bundler gem installed

## Installation Steps

1. **Install dependencies:**
   ```bash
   bundle install
   ```

2. **Set up the database:**
   ```bash
   rails db:create
   rails db:migrate
   ```

3. **Configure Twilio (Optional for testing):**
   
   The app works in test mode by default. To use real Twilio calls:
   
   Create a `.env` file in the root directory:
   ```
   TWILIO_ACCOUNT_SID=your_account_sid_here
   TWILIO_AUTH_TOKEN=your_auth_token_here
   TWILIO_PHONE_NUMBER=+15005550006
   TWILIO_TEST_MODE=true
   BASE_URL=http://localhost:3000
   ```
   
   **Note:** For testing, keep `TWILIO_TEST_MODE=true` to simulate calls without making real phone calls.

4. **Start the server:**
   ```bash
   rails server
   ```

5. **Visit the application:**
   Open your browser and go to: `http://localhost:3000`

## Testing

- The app includes a sample CSV file (`sample_numbers.csv`) with test numbers
- In test mode, calls are simulated and logged without making real phone calls
- Use dummy numbers like `1800xxxxxx` for testing

## Features

- Upload CSV files with phone numbers
- Paste numbers in textarea (supports newlines, commas, semicolons)
- AI prompt: Type "call 18001234567" to trigger calls
- Start/Stop call processing
- Real-time status updates
- Call log with status tracking

