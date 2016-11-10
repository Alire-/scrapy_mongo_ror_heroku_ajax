json.array!(@deals) do |deal|
  json.extract! deal, :id, :deal_name, :rest_name, :disc_info, :list_price, :pic_url
  json.url deal_url(deal, format: :json)
end
