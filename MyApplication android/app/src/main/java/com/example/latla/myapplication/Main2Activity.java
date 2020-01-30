package com.example.latla.myapplication;

import android.app.ProgressDialog;
import android.content.Intent;
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

public class Main2Activity extends AppCompatActivity {
    Button button2, button4;
    EditText Pass, eTmail;
    FirebaseAuth firebaseAuth;
    FirebaseAuth.AuthStateListener authStateListener;
    ProgressDialog pd;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        firebaseAuth = FirebaseAuth.getInstance();
        button2 = (Button) findViewById(R.id.button2);
        button4 = (Button) findViewById(R.id.button3);
        Pass = (EditText) findViewById(R.id.editText4);
        eTmail = (EditText) findViewById(R.id.editText3);
        pd = new ProgressDialog(this);
        authStateListener = new FirebaseAuth.AuthStateListener() {
            @Override
            public void onAuthStateChanged(@NonNull FirebaseAuth firebaseAuth) {
                if(firebaseAuth.getCurrentUser() != null){
                    startActivity(new Intent(Main2Activity.this,drawer.class));
                }
            }
        };


        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(Main2Activity.this,Register.class));
            }
        });

        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Signin();
            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        firebaseAuth.addAuthStateListener(authStateListener);
    }

    private void Signin() {
        final String emaile,pas;
        emaile = eTmail.getText().toString();
        pas = Pass.getText().toString();
        if(TextUtils.isEmpty(emaile)){
            Toast.makeText(Main2Activity.this,"Donner E-mail",Toast.LENGTH_LONG).show();
            return;
        }
        if(TextUtils.isEmpty(pas)){
            Toast.makeText(Main2Activity.this,"Donner mot de passe",Toast.LENGTH_LONG).show();
            return;
        }
        pd.setMessage("connexion en cours...");
        pd.show();
        firebaseAuth.signInWithEmailAndPassword(emaile,pas).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {
                    Toast.makeText(Main2Activity.this, "Bienvenu"+emaile, Toast.LENGTH_LONG).show();
                }
                else

                    Toast.makeText(Main2Activity.this,"acces refusé",Toast.LENGTH_LONG).show();

            }
        });
    }

}
