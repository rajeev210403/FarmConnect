package com.example.farmerapp;

import retrofit2.Call;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.POST;

public interface apiset {
    @FormUrlEncoded
    @POST("users")
    Call<responsemodel> getregister(
            @Field("username") String username,
            @Field("email") String emial,
            @Field("password") String password

    );
}
