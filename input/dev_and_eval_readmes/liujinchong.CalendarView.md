# CalenderView
Android上一个优雅、高度自定义、性能高效的日历控件，支持标记、自定义颜色、农历等。Canvas绘制，速度快、占用内存低

### Gradle
```
compile 'com.haibin:calendarview:1.0.6'
```
```
<dependency>
  <groupId>com.haibin</groupId>
  <artifactId>calendarview</artifactId>
  <version>1.0.6</version>
  <type>pom</type>
</dependency>
```
### 使用方法
```xml
 <com.haibin.calendarview.CalendarView
        android:id="@+id/calendarView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:min_year="2004"
        app:scheme_text="假"
        app:scheme_theme_color="@color/colorPrimary"
        app:selected_color="#30cfcfcf"
        app:selected_text_color="#333333"
        app:week_background="#fff"
        app:week_text_color="#111" />
```

### attrs
```xml
<declare-styleable name="CalendarView">
        <attr name="week_background" format="color" /> <!--星期栏的背景-->
        <attr name="week_text_color" format="color" /> <!--星期栏文本颜色-->
        <attr name="scheme_theme_color" format="color" /> <!--标记的颜色-->
        <attr name="current_day_color" format="color" /> <!--今天的文本颜色-->
        <attr name="scheme_text" format="string" />  <!--标记文本-->
        <attr name="lunar_text_color" format="color" /> <!--农历节假日颜色-->
        <attr name="selected_color" format="color" /> <!--选中颜色-->
        <attr name="selected_text_color" format="color" /> <!--选中文本颜色--> 
        <attr name="min_year" format="integer" />  <!--最小年份1900-->
        <attr name="max_year" format="integer" /> <!--最大年份2099-->
</declare-styleable>
```
### api
```java
public int getCurDay(); //今天
public int getCurMonth(); //当前的月份
public int getCurYear(); //今年
public void showSelectLayout(final int year); //快速弹出年份选择月份
public void closeSelectLayout(final int position); //关闭选择年份并跳转日期
public void setOnDateChangeListener(OnDateChangeListener listener);//添加事件
public void setOnDateSelectedListener(OnDateSelectedListener listener);//日期选择事件
public void setSchemeDate(List<Calendar> mSchemeDate);//标记日期
public void setStyle(int schemeThemeColor, int selectLayoutBackground, int lineBg);
public void update();//动态更新
```

### 效果预览
<img src="http://git.oschina.net/uploads/images/2017/0324/131748_aa249da8_494015.jpeg" height="650"/><img src="http://git.oschina.net/uploads/images/2017/0326/102135_52f0aecb_494015.jpeg" height="650"/> <img src="http://git.oschina.net/uploads/images/2017/0324/131818_4bf18f1c_494015.jpeg" height="650"/><img src="http://git.oschina.net/uploads/images/2017/0324/131825_ea1b41d5_494015.jpeg" height="650"/> 

## Licenses
- Copyright (C) 2013 huanghaibin_dev <huanghaibin_dev@163.com>
 
- Licensed under the Apache License, Version 2.0 (the "License");
- you may not use this file except in compliance with the License.
- You may obtain a copy of the License at
 
-         http://www.apache.org/licenses/LICENSE-2.0
 
- Unless required by applicable law or agreed to in writing, software
- distributed under the License is distributed on an "AS IS" BASIS,
- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
- See the License for the specific language governing permissions and
  limitations under the License.
