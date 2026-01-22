@smoke
Feature: Kullanıcı Girişi
  @positive
  Scenario: Kullanıcı geçerli bilgilerle giriş yapar
    Given kullanıcı login sayfasındadır
    When kullanıcı "standard_user" ve "secret_sauce" ile giriş yapar
    Then kullanıcı başarıyla giriş yapmış olur



    @negative
    Scenario Outline: Kullanıcı geçersiz bilgilerle giriş yapar
      Given kullanıcı login sayfasında
      When kullanıcı "invalid_user" ve "wrong_password" ile giriş yapar
      Then kullanıcı giriş yapamaz ve hata mesajı görür