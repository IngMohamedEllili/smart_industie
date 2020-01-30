package com.example.latla.myapplication;


import android.os.Bundle;
import android.provider.Settings;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CompoundButton;
import android.widget.Switch;
import android.widget.TextView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;


/**
 * A simple {@link Fragment} subclass.
 */
public class Controle extends Fragment {

    private DatabaseReference myRef,myRef1,myRef2,myRef3,myRef4,myRef6,myRef5;
    String switchon= "On";
    String switchoff= "Off";
    String var1="";
    String var2="";

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view= inflater.inflate(R.layout.fragment_controle, container, false);

        final Switch switch1 =view.findViewById(R.id.sLex);
        final Switch switch2 =view.findViewById(R.id.sLin);
        final Switch switch3 =view.findViewById(R.id.sLad);
        final Switch switch4 =view.findViewById(R.id.sLen);
        final Switch switch5 =view.findViewById(R.id.sVen);
        final Switch switch6 =view.findViewById(R.id.sBuzzer);
        final TextView textView1=view.findViewById(R.id.etlampeex);
        final TextView textView2=view.findViewById(R.id.etlampin);
        final TextView textView3=view.findViewById(R.id.etlampead);
        final TextView textView4=view.findViewById(R.id.etlampeen);
        final TextView textView5=view.findViewById(R.id.etventi);
        final TextView textView6=view.findViewById(R.id.etBuzzer);

        myRef5= FirebaseDatabase.getInstance().getReference("Controle").child("Buzzer");
        myRef5.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                if(dataSnapshot.getValue(String.class).equals("1")) {
                    switch6.setChecked(true);
                }else {
                    switch6.setChecked(false);
                }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });
        switch6.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {

                if (isChecked) {

                    myRef5.setValue("1");
                    textView6.setText(switchon);
                } else {
                    myRef5.setValue("0");
                    textView6.setText(switchoff);
                }
            }
        });

        if (switch6.isChecked()) {
            textView6.setText(switchon);
        } else {
            textView6.setText(switchoff);
        }

        myRef1= FirebaseDatabase.getInstance().getReference("Controle").child("LampeExt");
        myRef1.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {

                 if(dataSnapshot.getValue(String.class).equals("1")) {
                     switch1.setChecked(true);
                 } else  {

                     switch1.setChecked(false);
                 }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });

        switch1.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {

                if (isChecked) {

                    myRef1.setValue("1");
                    textView1.setText(switchon);
                } else {
                    myRef1.setValue("0");
                    textView1.setText(switchoff);
                }
            }
        });

        if (switch1.isChecked()) {
            textView1.setText(switchon);
        } else {
            textView1.setText(switchoff);
        }

        myRef2= FirebaseDatabase.getInstance().getReference("Controle").child("Lampes").child("LampeInterne");
        myRef6= FirebaseDatabase.getInstance().getReference("Capteurs").child("EtatLampe").child("EtatLampeInterieur");
        myRef6.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                if(dataSnapshot.getValue(String.class).equals("1")) {
                    textView2.setText(switchon);
                }else {
                    textView2.setText(switchoff);
                }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });

        myRef2.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {

                if(dataSnapshot.getValue(String.class).equals("1")){
                    switch2.setChecked(true);
                }else {
                    switch2.setChecked(false);
                }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });
        switch2.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    myRef2.setValue("1");
                    textView2.setText(switchon);
                } else {
                    myRef2.setValue("0");
                    textView2.setText(switchoff);
                }
            }
        });
        if (switch2.isChecked()) {
            textView2.setText(switchon);
        } else {
            textView2.setText(switchoff);
        }
        myRef3= FirebaseDatabase.getInstance().getReference("Controle").child("Lampes").child("LampeAdmin");
        myRef3.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {

                if(dataSnapshot.getValue(String.class).equals("1")){
                    switch3.setChecked(true);
                }else {
                    switch3.setChecked(false);
                }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });
        switch3.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked) {

                    myRef3.setValue("1");
                    textView3.setText(switchon);
                } else {
                    myRef3.setValue("0");
                    textView3.setText(switchoff);
                }
            }
        });
        if (switch3.isChecked()) {
            textView3.setText(switchon);
        } else {
            textView3.setText(switchoff);
        }
        myRef4= FirebaseDatabase.getInstance().getReference("Controle").child("Lampes").child("LampeEntre");

        myRef4.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {

                if(dataSnapshot.getValue(String.class).equals("1")){
                    switch4.setChecked(true);
                }else {
                    switch4.setChecked(false);
                }
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });
        switch4.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked) {
                    myRef4.setValue("1");
                    textView4.setText(switchon);
                } else {
                    myRef4.setValue("0");
                    textView4.setText(switchoff);
                }
            }
        });
        if (switch4.isChecked()) {
            textView4.setText(switchon);
        } else {
            textView4.setText(switchoff);
        }
        myRef= FirebaseDatabase.getInstance().getReference("Controle").child("Ventilateur");

        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {

                if(dataSnapshot.getValue(String.class).equals("1")){
                    switch5.setChecked(true);
                }else
                    switch5.setChecked(false);
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });
        switch5.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked){
                    myRef.setValue("1");
                    textView5.setText(switchon);
                }else {
                    myRef.setValue("0");
                    textView5.setText(switchoff);
                }
            }
        });
        if (switch5.isChecked()) {
            textView5.setText(switchon);
        } else {
            textView5.setText(switchoff);
        }
    return view;
    }

}