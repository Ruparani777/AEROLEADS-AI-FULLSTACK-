class CreateCalls < ActiveRecord::Migration[7.0]
  def change
    create_table :calls do |t|
      t.string :number, null: false
      t.string :status, default: 'pending'
      t.datetime :started_at
      t.datetime :finished_at
      t.string :twilio_sid
      
      t.timestamps
    end
    
    add_index :calls, :status
    add_index :calls, :number
    add_index :calls, :twilio_sid
  end
end

