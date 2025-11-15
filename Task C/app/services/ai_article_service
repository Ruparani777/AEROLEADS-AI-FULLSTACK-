require 'ruby/openai'

class AiArticleService
  def initialize(api_key = nil)
    @api_key = api_key || ENV['OPENAI_API_KEY']
    @client = OpenAI::Client.new(access_token: @api_key) if @api_key
  end

  def generate_article(title)
    return { error: 'OpenAI API key not configured' } unless @client

    prompt = build_prompt(title)
    
    begin
      response = @client.chat(
        parameters: {
          model: "gpt-4-turbo-preview", # Using gpt-4-turbo-preview for higher quality
          messages: [
            {
              role: "system",
              content: "You are a helpful programming blog writer. Write clear, beginner-friendly articles with code examples."
            },
            {
              role: "user",
              content: prompt
            }
          ],
          temperature: 0.8,
          max_tokens: 3000
        }
      )

      if response['choices'] && response['choices'][0]
        {
          success: true,
          content: response['choices'][0]['message']['content']
        }
      else
        { error: 'Unexpected API response format' }
      end
    rescue => e
      { error: e.message }
    end
  end

  private

  def build_prompt(title)
    <<~PROMPT
      Write a 700-1000 word beginner-friendly programming article titled: "#{title}"

      Requirements:
      - Include code examples in markdown format
      - Include a summary section
      - Include 3 key takeaways at the end
      - Use clear, simple language suitable for beginners
      - Make it engaging and practical
      - Format the content using proper markdown headings, lists, and code blocks

      Structure:
      1. Introduction
      2. Main content with examples
      3. Summary
      4. Key Takeaways (3 points)
    PROMPT
  end
end

