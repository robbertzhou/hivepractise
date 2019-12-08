package com.zy.udftest;

import org.apache.hadoop.hive.ql.exec.Description;
import org.apache.hadoop.hive.ql.exec.UDF;

import java.text.SimpleDateFormat;
import java.util.Date;

@Description(name = "zodiac",
value = "Example:\n" +
        "> select _FUNC_(date_string) from src;\n")
public class UDFZodiacSign extends UDF {
    public static void main(String[] args){
        UDFZodiacSign sign = new UDFZodiacSign();
        System.out.println(sign.evaluate("2015-09-16 12:11:11"));
    }
    private SimpleDateFormat sdf;

    public UDFZodiacSign(){
        sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    }

    public String evaluate(Date date){
        return evaluate(date.getMonth(),date.getDay());
    }

    public String evaluate(String date){
        Date dt = null;
        try{
            dt = sdf.parse(date);
        }catch (Exception ex){
            return null;
        }
        return this.evaluate(dt.getMonth(),dt.getDay());
    }

    public String evaluate(Integer month,Integer day){
        return "黄道吉日";
    }
}
