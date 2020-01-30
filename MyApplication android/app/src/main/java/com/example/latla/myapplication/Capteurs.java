package com.example.latla.myapplication;


import android.nfc.Tag;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.Toolbar;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;


/**
 * A simple {@link Fragment} subclass.
 */
public class Capteurs extends Fragment {


    private DatabaseReference myRef;


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment

        View view=inflater.inflate(R.layout.fragment_capteurs, container, false);

        final TextView textView=view.findViewById(R.id.temperature);
        final TextView textView1=view.findViewById(R.id.humidite);
        final TextView textView2= view.findViewById(R.id.gazdet);
        final TextView textView3=view.findViewById(R.id.mouvement);
        myRef=FirebaseDatabase.getInstance().getReference("Capteurs").child("PIR");
        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                String value2=dataSnapshot.getValue(String.class);

                if(value2.equals("0")) {
                    textView3.setText("pas de mouvement");
                } else {
                     textView3.setText("mouvement detecté");
                }

            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });
        myRef=FirebaseDatabase.getInstance().getReference("Capteurs").child("Gaz");
        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                String value3 = dataSnapshot.getValue(String.class);
                if (value3.equals("0")) {
                    textView2.setText("pas de gaz");
                } else {
                    textView2.setText("Alert");
                }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });


        myRef= FirebaseDatabase.getInstance().getReference("Capteurs").child("Humidite");

        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                Long value1=dataSnapshot.getValue(Long.class);
                textView1.setText(value1+"");
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });
        myRef= FirebaseDatabase.getInstance().getReference("Capteurs").child("Temperature");
        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {

                 Long value=dataSnapshot.getValue(Long.class);
                 textView.setText(value+"");

            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });


        return view;


    }

}
