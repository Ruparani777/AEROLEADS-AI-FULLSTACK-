class CreatePosts < ActiveRecord::Migration[7.1]
  def change
    create_table :posts do |t|
      t.string :title
      t.text :content
      t.string :status, default: 'draft' # draft, generating, published
      t.text :generation_log
      t.timestamps
    end
  end
end

