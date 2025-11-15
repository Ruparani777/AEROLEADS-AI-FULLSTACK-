class BlogController < ApplicationController
  before_action :set_post, only: [:show, :edit, :update, :save_draft]

  def index
    @posts = Post.recent
  end

  def show
    @post = Post.find(params[:id])
  end

  def new
    @post = Post.new
  end

  def create
    # This action handles the initial form submission
    redirect_to new_blog_path
  end

  def generate_articles
    titles_text = params[:titles] || ''
    titles = titles_text.split("\n").map(&:strip).reject(&:empty?)
    
    if titles.empty?
      render json: { success: false, error: 'No titles provided' }, status: :unprocessable_entity
      return
    end

    generated_posts = []
    errors = []

    titles.each_with_index do |title, index|
      post = Post.create!(
        title: title,
        status: 'generating',
        content: '',
        generation_log: "Starting generation for: #{title}\n"
      )

      begin
        service = AiArticleService.new
        result = service.generate_article(title)

        if result[:success]
          post.update!(
            content: result[:content],
            status: 'draft',
            generation_log: post.generation_log + "✓ Successfully generated\n"
          )
          generated_posts << post
        else
          post.update!(
            status: 'draft',
            content: "Error generating article: #{result[:error]}",
            generation_log: post.generation_log + "✗ Error: #{result[:error]}\n"
          )
          errors << { title: title, error: result[:error] }
        end
      rescue => e
        post.update!(
          status: 'draft',
          content: "Error: #{e.message}",
          generation_log: post.generation_log + "✗ Exception: #{e.message}\n"
        )
        errors << { title: title, error: e.message }
      end

      # Add a small delay to avoid rate limiting
      sleep(1) if index < titles.length - 1
    end

    render json: {
      success: true,
      generated: generated_posts.count,
      errors: errors.count,
      posts: generated_posts.map { |p| { id: p.id, title: p.title, status: p.status } }
    }
  end

  def edit
    @post = Post.find(params[:id])
  end

  def update
    if @post.update(post_params)
      redirect_to blog_path(@post), notice: 'Article updated successfully.'
    else
      render :edit
    end
  end

  def save_draft
    if @post.update(post_params.merge(status: 'published'))
      render json: { success: true, message: 'Article saved and published.' }
    else
      render json: { success: false, errors: @post.errors.full_messages }
    end
  end

  def generation_log
    @post = Post.find(params[:id])
    render json: { log: @post.generation_log || 'No log available' }
  end

  private

  def set_post
    @post = Post.find(params[:id])
  end

  def post_params
    params.require(:post).permit(:title, :content, :status)
  end
end

