package com.gitee.jack20081117.frog.egg;

import java.io.Serializable;

public class CellGroup implements Serializable{
    private static final long serialVersionUID=1L;
    public Zone groupInputZone;
    public Zone groupOutputZone;
    public float cellInputRadius;
    public float cellOutputRadius;
    public int cellQty;
    public int inputQtyPerCell;
    public int outputQtyPerCell;
}
