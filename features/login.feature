@smoke
Feature: Kullanıcı Girişi
  @positive
  Scenario: Kullanıcı geçerli bilgilerle giriş yapar
    Given kullanıcı login sayfasındadır
    When kullanıcı "standard_user" ve "secret_sauce" ile giriş yapar
    Then kullanıcı başarıyla giriş yapmış olur



