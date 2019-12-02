package com.zy.prestotest;

import com.facebook.presto.jdbc.PrestoDriver;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class QueryTest {
    public static void main(String[] args){
        try {

            Class.forName("com.facebook.presto.jdbc.PrestoDriver");
            Connection connection = DriverManager.getConnection("jdbc:presto://master.zy.com:8099/hive/default","hive",null);
            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery("select * from airports");
            while (rs.next()){
                System.out.println(rs.getString(1));
            }
        }catch (Exception ex){
            ex.printStackTrace();
        }
    }
}
