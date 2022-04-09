# پروژه فروشگاه آنلاین
در اینجا یک پروژه فروشگاهی را توسط فریمورک جنگو پیاده سازی کرده ام. برای قالب پروژه از قالب رایگانی که در قسمت bootstrap سایت
w3schools.com
قرار داده شده و بصورت رایگان در دستسرس عموم قرار دارد، استفاده کرده ام.   
پروژه فوق در هاست رایگان سایت python any where آپلود شده است که از طریق لینک زیر میتواند پروژه را مشاهده نمایید:
[https://mohammadaq.pythonanywhere.com/](https://mohammadaq.pythonanywhere.com)
## منوی Nav Bar
منوی Nav Bar شامل ۶ گزینه میباشد:  
الف) خانه: صفحه اصلی سایت  
 ب) لپ تاپ: لیست همه محصولات دسته بندی لپ تاپ  
ج)  موبایل: لیست همه محصولات دسته بندی موبایل  
د) رجیستر: در صورتی که کاربر تاکنون ثبت نام نکرده باشد، با مراجعه به این قسمت به صفحه ثبت نام هدایت میشود.  
ه)  لاگین: درصورتی که کابر قبلا در سایت ثبت نام کرده باشد با مراجعه به این قسمت به صفحه لاگین هدایت میشود.  
ی)  قسمت جستجو: کاربر با وارد کردن کلمه یا کلمات کلیدی مورد نظر خود در قسمت جستجو می تواند لیستی از محصولات هماهنگ با کلمه یا کلماتی را که وارد کرده است مشاهده کند.  
** لازم به ذکر است که در صورت لاگین کردن کاربر؛ دو گزینه ثبت نام و لاگین جای خود را به دو گزینه سبد خرید و خروج می دهند.  

## لیست محصولات (لپ تاپ و موبایل) 

لیست محصولات هر دسته بندی؛ تمام محصولات دسته بندی مربوطه می باشد که شامل تصویر، عنوان،  قیمت و دکمه خرید می باشد. لازم به ذکر است که در صورت موجود نبودن هر محصول به جای قیمت آن محصول عبارت "محصول موجود نمیباشد" نمایش داده می شود.  
 هر صفحه لیست دسته بندی شامل ۱۲ محصول از دسته بندی مورد نظر می باشد.  
 همچنین کاربران می‌توانند در قسمت مرتب‌سازی انتخاب کنند که لیست محصولات بر چه اساسی مرتبط شود. سه روش مرتبط مرتب سازی در این قسمت آماده شده است:  
الف) فقط محصولات موجود نمایش داده شوند   
ب) محصولات از کمترین قیمت به بالاترین قیمت نمایش داده شود   
ج) محصولات از بالاترین قیمت به پایین ترین قیمت نمایش داده شود

## جزییات هرمحصول، افزودن محصول به سبد خرید

 کاربر می‌تواند با کلیک بر روی دکمه خرید؛ جزئیات محصول را مشاهده و اقدام به خرید آن محصول به تعداد مورد نیازش نماید. همچنین برای انجام عملیات خرید محصول دو شرط باید رعایت شود:  
 الف) محصول موجود باشد   
ب) کاربر در سایت لاگین کرده باشد  
در صورت برقرار نبودن شرط "الف" کاربر با پیغام "محصول در دسترس نمی‌باشد" مواجه می‌شود. همچنین در صورت برقرار نبود شرط "ب" کاربر با پیغام "لطفا برای خرید لاگین کنید" مواجه می‌شود. که با کلیک بر روی کلمه لاگین به صفحه لاگین هدایت می‌شود.  
 در صورت برقرار بودن شروط بالا کاربر میتواند با توجه به نیاز خود؛ تعداد محصول مورد نظر خود را انتخاب کرده و روی دکمه خرید کلیک کند. با اینکار محصول مورد نظر در سبدخرید وی ذخیره میشود.  
 لازم به ذکر است که کاربران نمی توانند در فرآیند خرید هر محصول بیشتر از تعدادی که در انبار (پایگاه داده) موجود است خرید کنند.    
 
 ## ارسال نظر

 هر کاربر پس از لاگین کردن میتواند نظر خود را در مورد محصولات سایت ارسال کند. نظر کاربران بلافاصله در صفحه نظرات نمایش داده نمی شود. بلکه در پایگاه داده ذخیره شده و با نظر مدیر سایت در قسمت نظرات به نمایش در می‌آید.  
  ## نهایی کردن خرید

 برای مشاهده محصولاتی که کاربر به سبد خرید خود اضافه کرده است، باید از منوی Nav Bar بر روی گزینه سبد خرید کلیک کند. درصورتی که قبلا محصولی را خریداری نکرده باشد، با پیغام "سبد خرید شما خالی است" مواجه می‌شود. در غیر اینصورت کاربر لیست محصولاتی را که به سبد خرید اضافه کرده است را مشاهده می‌کند. کاربر در اینجا می‌تواند در صورت تمایل تعداد هر محصول را کم، زیاد و یا حذف نماید.  
 در نهایت کاربر با کلیک بر روی دکمه 'تمام' فاکتور سبد خرید خود را مشاهده می‌کند. و چنانچه کاربر قصد نهایی کردن خرید خود را داشته باشد با کلیک بر روی گزینه پرداخت به صفحه پرداخت می رود.  

