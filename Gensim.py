import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
 
from gensim.summarization import summarize
 
# http://www.neokur.com/kitap/4972/suc-ve-ceza/kitap-incelemeleri
text = """
Raskolnikov Rusya’nın ufak bir yerinden Petersburg’a hukuk okumaya gelmiş, geleceğe ışıkla bakan biridir. Raskolnikov okulunu bitirip ailesini ve kendi hayatını maddi sıkıntılardan kurtarmayı düşünmektedir fakat okul zamanı yaşadığı maddi sıkıntılar bize Raskolnikov için ‘’eski bir hukuk öğrencisidir’’ cümlesini kurduracaktır. Raskolnikov’un ailesinden gelen ve özel ders vererek kazandığı para dışında bir geliri yoktur. Zamanla yaşanılan olumsuz durumlarla maddi darlığa düşen Raskolnikov okulunu bırakmak zorunda kalır. Bu sırada psikolojik bir bunalıma giren Raskolnikov zamanla kaldığı odanın kirasını vermekte bile zorluklar yaşar.

Raskolnikov paraya ihtiyaç duyduğunda rehinci bir yaşlı kadına eşya rehin eder. Rehinci yaşlı kadın, toplum için hiçbir işe yaramayan, insanların düştüğü maddi sıkıntıları fırsat bilip onların bu zayıflıkları ile para kazanan biridir. Rehinci kadın kazandığı parayı öldüğünde bir kiliseye bağışlanması vasiyet edip, yaptığı bunca kötülükle cennete gitmeyi düşünmektedir. Daha sonra içerisinde bulunduğu maddi sıkıntılar ve yaşadığı psikolojik bunalımlar Raskolnikov’a bir cinayet fikri uyandırır. Raskolnikov bu kadını öldürmenin topluma faydalı bir hizmet olduğunu düşünmektedir.

Raskolnikov bir gün rehinci kadına tıpkı bir eşyayı rehin vermeye gittiği gibi gidip kafasında bir cinayet planı oluşturacaktır. Eşyaları hangi sandıkta ve nerede sakladığını, sandık anahtarının nerede olduğunu ve bu cinayeti nasıl işleyebileceğini düşünür ve bir plan kurar. Kimi zaman bu cinayet fikrinden vazgeçer.

Bir meyhanede yaşlı bir adamla sohbete giren Raskolnikov’a yaşlı adam kendisinden bahseder, bir kızının olduğunu ve bedenini satarak ailesine bakmaya çalıştığını söyler. Bunu duyan Raskolnikov şok olmuştur, ardından annesinden gelen bir mektupta kız kardeşinin birisiyle nişanlandığı, nişanlısının zengin olduğunu ve artık bu maddi sıkıntılardan kurtulacaklarını, kendilerinin de Petersburg’a geleceğinden bahsetmektedir. Raskolnikov bu mektuba hiç sevinmez ve tıpkı meyhanede karşılaştığı yaşlı adamın kızı ile kendi kız kardeşini aynı keseye koyar. Kız kardeşi de ailesi için aşık olmadığı birisiyle evleneceği fikri onu rahatsız etmektedir. Zaman zaman cinayetten vazgeçse de yaşanılan olaylar ve içinde bulunduğu psikolojik durum bu cinayeti kaçınılmaz kılar.

Raskolnikov bir balta ile yaşlı kadını öldürüp daha sonra rehin eşyaları çalacak ve toplum için bir iyilik yapacaktır. Planı gerçekleştirmek için rehinciye tıpkı rehin verecek gibi giden Raskolnikov eve girer ve rehinciyi balta ile öldürür. Rehin eşyalardan bir miktar çaldıktan sonra beklenmeyen bir kadın -rehincinin kız kardeşi- kapıdan içeri girer ve kadın yaşlı rehincinin öldürüldüğünü görür, ardından Raskolnikov bu kadını da orada baltalayarak öldürmek zorunda kalır. Artık suç işlenmiştir, çaldığı rehin eşyaları bir taşın altına gömer ve kirada kaldığı odasına gidip uyur.

Olaylar buradan sonra gelişmeye devam eder. Kimin katil olduğuna dair bir kanıt bulunmaz, birilerinden şüphelenilir ancak Raskolnikov’dan şüphelenen olmaz. Raskolnikov işlediği cinayet ve vicdanı ile başbaşa kalır. Artık o bir katildir ve vicdanı onu rahat bırakmaz. Kitap bundan sonra bu olaylar çerçevesinde gelişmektedir. Buradan sonrasını sizin okuyup kendi düşüncelerinizle yorumlamanız daha iyi olacaktır.

Kitap için yorumuma gelecek olursak, kitapta aslında arada kalmış bir karakter görmekteyiz. Kendisini bulunduğu mevkiye layık görmeyen ama şartlardan dolayı layık olduğu mevkiye de yükselemeyen karakterin çırpınışlarını daha ilk sayfalarda hissediyoruz. Kitapta bu arada kalmış karakterin cinayeti işlemeden ve işledikten sonraki psikolojik durumunu yazar bizlere çok iyi sunuyor. Suç işlenmeden önce sahip olduğu psikolojik durum zaten kötüyken işlenilen suç ile bu durum daha da kötüleşiyor ve bunu kitabı okurken birebir şahit oluyoruz.

Kitabı okurken işlenilen suçun doğru olup olmadığını kendime sormadım değil. O psikolojide ben olsam ne yapardım bunu da düşündüm. Bir suç ne kadar güzel planlanırsa planlansın, hiçbir delil ortada bırakılmasın, yakalanmanız da mümkün olmasın diye kabul etsek bile o suçu işleyen olarak vicdanımızın bunu biliyor olması bize gereken cezayı verecektir. Bunun çerçevesinde düşündüğümüz zaman sanırım suç işlemek göründüğü kadar basit olmayan bir eylem. En azından suçu işledikten sonra gelişen olaylar ve insanın kendi vicdanı ile olan savaşı bize verilen en büyük ceza olarak düşünüyorum.

Bununla beraber karakterimizin geleceğe dönük güzel planlarının olması ve başarılı bir kişi olması ise onun böyle bir suçu işlemeye hiçbir hakkı yokmuş gibi bir duruma sokuyor. Yani karakterden beklenti yüksek olunca onu böyle bir suçla toplumun kabul etmeyeceği düşüncesi kafasını sarıyor.

Aslında kitap da karakterimizin psikolojik durumunun toplumun baskısından da nasıl etkilediğini görüyoruz. Sürekli toplumdan uzaklaşma isteği ve kendini kimseye anlatamaması, anlatsa bile kimsenin onu anlayamayacağı düşüncesini ile girilen yalnızlık da gözler önüne seriliyor. Toplumdaki sınıfların suça ne kadar yatkın olduğu genel olarak kitapta görülürken özellikle kitabın bir kısmında yaşanılan hırsızlığa benzer bir olayla iyice vurgulanıyor.

Kitabın bir başka kısmında ise suç üzerine Raskolnikov birisiyle konuşuyor. Bu kısımda suç ve suçlu üzerine olan farklı bir diyalog var. Açıkçası kitabın en sevdiğim kısımlarından birisi de burasıydı.

Kitabı çok uzun bir zaman aralığında okuduğum için belli başlı sıkıntılar yaşadım, yazacaklarıma siz kitabı okurken dikkat ederseniz sizin için daha doyurucu bir okuma olabilir. Kitabın içerisinde birçok yan hikaye var, bu yan hikayeler kitabın ilerisinde rayına oturmaya başlıyor ama uzun bir zaman aralığında okumamdan dolayı bu yan hikayelerdeki detaylar benden çabuk silindi ve bu yan hikayeleri rayına oturttururken zorluk yaşadım. Ayrıca kitapta bulunan karakterlerin birden fazla isimleri var ve isimlerin yabancı olması, birbirine benzemesinden dolayı sürekli bu kimdi diye çelişkiye düştüm. Karakterleri hatırlamakta epey beni yordu. Ve itiraf etmeliyim ki olayları ve kişileri hatırlamak için kimi zaman internetten yardım aldım.

Dünya klasiği olma ünvanını sonuna kadar hak eden ve derin psikolojik tahlilleri olan bir kitaptı. Ayrıca bu kitap bitince içimde bir hüzün de oluştu. Böyle bir eseri tekrar aynı heyecanla okumam mümkün olmayacak sanırım fakat bu eseri okumanın da bana kattığı çok şey olduğunu düşünerek bir yandan da bu hüzün yok oldu. Uzun ve keyifli bir maratondu. Sanırım ileri tekrar okuyacağım ve kitaplığımın en güzel yerinde duracak eserler arasında oldu.
"""

print ('Input text:')
print (text)
 
print ('Summary:')
print (summarize(text))
 
print ('Summary: ratio=0.5')
print (summarize(text, ratio=0.5))
 
print ('Summary: ratio=0.25')
print (summarize(text, ratio=0.25))
 
print ('Summary: word_count=50')
print (summarize(text, word_count=50))
 
from gensim.summarization import keywords
 
print ('Keywords:')
print (keywords(text))
