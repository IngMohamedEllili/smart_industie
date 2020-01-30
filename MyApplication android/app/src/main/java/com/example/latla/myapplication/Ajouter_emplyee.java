package com.example.latla.myapplication;


import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;


/**
 * A simple {@link Fragment} subclass.
 */
public class Ajouter_emplyee extends Fragment {
    private DatabaseReference myRef;
     Button btn ;
     EditText nom ;
     EditText prenom ;
     EditText carte_rfid;
     EditText Mot_passe;



    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View rootview=inflater.inflate(R.layout.fragment_ajouter_emplyee, container, false);


        btn= (Button) rootview.findViewById(R.id.ajout);
        prenom= rootview.findViewById(R.id.ePrenom);
        nom= rootview.findViewById(R.id.eNom);
        Mot_passe= rootview.findViewById(R.id.eKey);
        carte_rfid=rootview.findViewById(R.id.eRfid);

        myRef= FirebaseDatabase.getInstance().getReference("employees");
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String key = myRef.push().getKey();
                Employe employe = new Employe();

                String Prenom =prenom.getText().toString();
                employe.setPrenom(Prenom);

                String Nom = nom.getText().toString();
                employe.setNom(Nom);

                String Rfid = carte_rfid.getText().toString();
                employe.setN_carte_rfid(Rfid);

                String passw = Mot_passe.getText().toString();
                employe.setMot_de_passe(passw);

                myRef.child(key).setValue(employe);
            }
        });


        return  rootview;
    }

}