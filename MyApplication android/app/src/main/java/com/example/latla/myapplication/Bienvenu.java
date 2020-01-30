package com.example.latla.myapplication;


import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;


/**
 * A simple {@link Fragment} subclass.
 */
public class Bienvenu extends Fragment {


    private DatabaseReference myRef;
    public Bienvenu() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view= inflater.inflate(R.layout.fragment_bienvenu, container, false);
        final Button btn= view.findViewById(R.id.act);
        final Button btn1= view.findViewById(R.id.desact);

        myRef= FirebaseDatabase.getInstance().getReference("Activation_Systeme").child("Activation_Systeme_Total");
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                myRef.setValue("1");
            }
        });
        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                myRef.setValue("0");
            }
        });

    return view;
    }

}
