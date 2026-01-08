Feature: Kullanıcı Girişi

Background: ##Her senaryodan önce otomatik çalışan ortak adımlar.Tekrar eden Given adımlarını azaltır
  Given Kullanıcı giriş sayfasındadır

Scenario: Geçerli bilgilerle giriş
  When Kullanıcı doğru kullanıcı adı ve şifre girer
  Then Kullanıcı ana sayfaya yönlendirilmelidir

Scenario Outline: Geçersiz bilgilerle giriş ##“Aynı davranışı farklı verilerle test et”
  When Kullanıcı <kullaniciAdi> ve <sifre> girer
  Then Hata mesajı gösterilmelidir

Examples:
  | kullaniciAdi | sifre   |
  | admin        | 123     |
  | test         | yanlış  |
