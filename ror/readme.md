# Important Memo

* Use Mongo DB online service instead of local Mongo DB

  * config/mongoid.yml
  > line 13 ~ line 21
  >
  > line 146 ~ line 154

* To support the heroku.com online host production environment

  * Gemfile
  > line 7 ~ line 12

* CORS support

  * Gemfile
  > line 57: gem 'rack-cors', require: 'rack/cors'

  * config/application.rb
  > line 25 ~ line 33
  ```
  config.middleware.insert_before 0, "Rack::Cors" do
    allow do
      origins '*'
        resourse '*', headers: :any, methods: [:get]
      end
    end
  end
  ```
