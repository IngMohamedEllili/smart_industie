package com.example.latla.myapplication;

import android.app.ProgressDialog;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseAuthException;

public class Register extends AppCompatActivity {
    private EditText Pass, eTmail;
    private Button button4;
    private FirebaseAuth mAuth;
    ProgressDialog progressDialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        mAuth = FirebaseAuth.getInstance();
        progressDialog = new ProgressDialog(this);
        Pass = (EditText) findViewById(R.id.Pass);
        eTmail = (EditText) findViewById(R.id.eTmail);
        button4 = (Button) findViewById(R.id.button4);

        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               String email = eTmail.getText().toString();
               String  passw = Pass.getText().toString();
                UserRegister(email,passw);
            }


        });
    }
    private void UserRegister(String email,String passw) {

        if(TextUtils.isEmpty(email)||TextUtils.isEmpty(passw)){
            Toast.makeText(Register.this,"inserer email",Toast.LENGTH_LONG).show();
            return;
        }
        progressDialog.setMessage("inscription en cours ...");
        progressDialog.show();

       mAuth.createUserWithEmailAndPassword(email,passw).addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful())
                {
                    Toast.makeText(Register.this,"inscription avec succes",Toast.LENGTH_LONG).show();
                }
                else
                    Toast.makeText(Register.this,"inscription sans succes",Toast.LENGTH_LONG).show();

            }
        });
    }
}
