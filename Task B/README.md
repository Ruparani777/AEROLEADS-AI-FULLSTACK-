# Autodialer - Ruby on Rails + Twilio

A Rails application for managing automated phone calls with Twilio integration.

## Features

- 📤 Upload phone numbers via CSV file or textarea
- 🚀 Start/Stop call processing
- 📊 Real-time call status logging
- 🤖 AI prompt interface - type "call 1800xxxxxx" to trigger calls
- 📞 Sequential call processing via background jobs
- 🔄 Live status updates with AJAX polling

## Setup

### Prerequisites

- Ruby 3.0+ 
- Rails 7.0+
- SQLite3
- Twilio account (for production) or use test mode

### Installation

1. Install dependencies:
```bash
bundle install
```

2. Set up the database:
```bash
rails db:create
rails db:migrate
```

3. Configure Twilio (optional for testing):
Create a `.env` file or set environment variables:
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+15005550006
TWILIO_TEST_MODE=true
BASE_URL=http://localhost:3000
```

**Important**: For testing, the app uses test mode by default. Set `TWILIO_TEST_MODE=true` to simulate calls without making real phone calls.

4. Start the server:
```bash
rails server
```

5. Visit `http://localhost:3000`

## Usage

### Uploading Numbers

1. **CSV Upload**: Upload a CSV file with phone numbers in the first column
2. **Textarea**: Paste numbers separated by newlines, commas, or semicolons

### Starting Calls

1. Click "Start Calls" to begin processing the queue
2. Calls are processed sequentially
3. Click "Stop Calls" to halt processing

### AI Prompt

Type commands like:
- "call 18001234567"
- "make a call to 1-800-123-4567"
- "call +1 800 123 4567"

The app will extract the phone number and initiate a call.

### Call Statuses

- `pending`: Waiting to be processed
- `queued`: In the call queue
- `ringing`: Call is ringing
- `in_progress`: Call is active
- `completed`: Call finished successfully
- `failed`: Call failed
- `busy`: Line was busy
- `no_answer`: No answer
- `canceled`: Call was canceled

## Testing

**IMPORTANT**: The app is configured to use test mode by default. In development, calls are simulated and no real phone calls are made. This prevents calling real people during testing.

To enable real Twilio calls:
1. Set up a Twilio account
2. Configure your credentials in environment variables
3. Set `TWILIO_TEST_MODE=false` or remove it
4. Use verified phone numbers (Twilio trial accounts have restrictions)

## Twilio Configuration

For production use:
1. Get your Twilio Account SID and Auth Token from the Twilio Console
2. Purchase a Twilio phone number
3. Set up webhook URLs for TwiML responses
4. Configure your BASE_URL to point to your server

The app includes TwiML endpoints at:
- `/twiml/voice` - Voice response handler
- `/twiml/status` - Status callback handler

## License

MIT

