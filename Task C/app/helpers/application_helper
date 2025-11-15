module ApplicationHelper
  def markdown(text)
    return '' if text.blank?
    
    renderer = Redcarpet::Render::HTML.new(
      filter_html: false,
      hard_wrap: true,
      prettify: true
    )
    
    markdown = Redcarpet::Markdown.new(renderer, {
      autolink: true,
      tables: true,
      fenced_code_blocks: true,
      strikethrough: true,
      superscript: true,
      underline: true,
      highlight: true,
      quote: true,
      footnotes: true
    })
    
    markdown.render(text).html_safe
  rescue
    simple_format(text)
  end
end

