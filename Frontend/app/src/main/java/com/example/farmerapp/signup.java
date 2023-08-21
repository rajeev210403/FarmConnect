package com.example.farmerapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class signup extends AppCompatActivity {
    TextView already;
    Button btn;
    EditText nametext , emailtext, passwordtext;
    Button sgb;
    TextView tv ;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);
        nametext=findViewById(R.id.username);
        emailtext = findViewById(R.id.signupemail);
        passwordtext = findViewById(R.id.signuppassword);
        btn = findViewById(R.id.signupbutton);
        tv=findViewById(R.id.atv);

        already = findViewById(R.id.alreadyuser);
        sgb = findViewById(R.id.signupbutton);
        already.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(signup.this, login.class);
                startActivity(intent);
            }
        });

        sgb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(signup.this, MainActivity.class);
                startActivity(intent);
            }
        });

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                processdata(nametext.getText().toString(), emailtext.getText().toString(), passwordtext.getText().toString());
            }
        });
    }
    public void processdata(String name, String email, String password){
        Call<responsemodel> call = apiController.getInstance()
                .getapi()
                .getregister(name,email,password);
        call.enqueue(new Callback<responsemodel>() {
            @Override
            public void onResponse(Call<responsemodel> call, Response<responsemodel> response) {
                responsemodel obj = response.body();
                tv.setText(obj.getMessage());
                nametext.setText("");
                emailtext.setText("");
                passwordtext.setText("");
            }

            @Override
            public void onFailure(Call<responsemodel> call, Throwable t) {

                tv.setText("something went wrong");
                nametext.setText("");
                emailtext.setText("");
                passwordtext.setText("");
            }
        });
    }
}