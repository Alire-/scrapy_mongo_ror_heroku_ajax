class Deal
  include Mongoid::Document
  field :deal_name, type: String
  field :rest_name, type: String
  field :list_price, type: String
  field :disc_info, type: String
  field :pic_url, type: String
end
