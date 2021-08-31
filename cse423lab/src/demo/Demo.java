package demo;

import com.jogamp.opengl.GL2;
import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.GLCapabilities;
import com.jogamp.opengl.GLEventListener;
import com.jogamp.opengl.GLProfile;
import com.jogamp.opengl.awt.GLCanvas;
import com.jogamp.opengl.glu.GLU;
import java.lang.Math;
import javax.swing.JFrame;
import java.util.Random;



public class Demo {

    public static void main(String args[]) {
        // getting the capabilities object of GL2 profile
        final GLProfile profile = GLProfile.get(GLProfile.GL2);
        GLCapabilities capabilities = new GLCapabilities(profile);
        // The canvas
        final GLCanvas glcanvas = new GLCanvas(capabilities);
        //ThirdGLEventListener b = new ThirdGLEventListener();
        lab1 l = new lab1();
        //glcanvas.addGLEventListener(b);
        glcanvas.addGLEventListener(l);
        glcanvas.setSize(400, 400);
        // creating frame
        final JFrame frame = new JFrame("Demo");
        // adding canvas to frame
        frame.add(glcanvas);
        frame.setSize(1000, 480);
        frame.setVisible(true);
    }
}

class lab1 implements GLEventListener {
    private GLU glu;
    public void init(GLAutoDrawable gld) {
        GL2 gl = gld.getGL().getGL2();
        glu = new GLU();

        gl.glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
        gl.glViewport(-250, -150, 250, 150);
        gl.glMatrixMode(GL2.GL_PROJECTION);
        gl.glLoadIdentity();
        glu.gluOrtho2D(-300.0, 300.0, -300, 300.0);
    }

    public void display(GLAutoDrawable drawable) {
        GL2 gl = drawable.getGL().getGL2();

        draw50points(gl);
        drawHouse(gl);
        drawTails(gl);
   
    }
    
    private void draw50points(GL2 gl){
        gl.glClear(GL2.GL_COLOR_BUFFER_BIT);
        gl.glColor3d(1, 0, 0);
        gl.glPointSize(2.0f);
        gl.glBegin(GL2.GL_POINTS);  
        Random rd = new Random();
        int lowerBound = 1;
        int upperBound = 51;
        for (int i = 0; i < 50; i++) {
            int x = rd.nextInt(upperBound);
            int y = rd.nextInt(upperBound);

            gl.glVertex2d(x, y);
        }
        gl.glEnd();
    }
    
    private void drawTails(GL2 gl){
        gl.glBegin(GL2.GL_POINTS);
        gl.glPointSize(3.0f);
        gl.glColor3d(1, 0, 0);
        
        DDA(gl, 150, 100, 150, -100, false); //vertical straight line
        DDA(gl, 80, 100, 230, 100, true);   //horizontal dashed line
        gl.glEnd();
    }
    
    private void DDA(GL2 gl, float x1, float y1, float x0, float y0, boolean d){
        
      
        float dx = x1 - x0;
        float dy = y1 - y0;
        
        float steps = Math.abs(dx) > Math.abs(dy) ? Math.abs(dx) : Math.abs(dy);
        
        float xinc = dx/ (float) steps;
        float yinc = dy/ (float) steps;
        
        float x = x0;
        float y = y0;
        
        for(int i =0; i<=steps; i++){
            
            if(d){
                if(i%2==0){
                   gl.glVertex2d((float) x, (float) y);
                }
                x += xinc;
                y += yinc;
            }else{
               gl.glVertex2d((float) x, (float) y);
               x += xinc;
               y += yinc;
            }
            
        }
        
    }
    
    
    private void drawHouse(GL2 gl){
        gl.glBegin(GL2.GL_TRIANGLES);
        gl.glPointSize(3.0f);
        gl.glColor3d(0, 2, 0);
        gl.glVertex2d(-280, 150);
        gl.glVertex2d(-180, 250);
        gl.glVertex2d(-80, 150);
        gl.glEnd();
        
        gl.glBegin(GL2.GL_LINES);
        gl.glClear(GL2.GL_COLOR_BUFFER_BIT);
        gl.glPointSize(10.0f);
        gl.glColor3d(2, 0, 0);
        
        gl.glVertex2d(-280, 0); //left wall
        gl.glVertex2d(-280, 150);//left wall
        
        gl.glVertex2d(-80, 0);//left wall
        gl.glVertex2d(-80, 150);//left wall
        
        gl.glVertex2d(-280, 0);//right wall
        gl.glVertex2d(-80, 0);//right wall
        
        gl.glVertex2d(-160, 0);//right wall
        gl.glVertex2d(-160, 100);//right wall
        
        gl.glVertex2d(-200, 0); //door
        gl.glVertex2d(-200, 100);//door
        
        gl.glVertex2d(-160, 100);//door
        gl.glVertex2d(-200, 100);//door
        
        gl.glVertex2d(-230, 80);//left window
        gl.glVertex2d(-250, 80);//left window
        
        gl.glVertex2d(-230, 120);//left window
        gl.glVertex2d(-250, 120);//left window
        
        gl.glVertex2d(-230, 120);//left window
        gl.glVertex2d(-230, 80);//left window
        
        gl.glVertex2d(-250, 120);//left window
        gl.glVertex2d(-250, 80);//left window
        
        
        
        gl.glVertex2d(-130, 80);//right window
        gl.glVertex2d(-110, 80);//right window
        
        gl.glVertex2d(-130, 120);//right window
        gl.glVertex2d(-110, 120);//right window
        
        gl.glVertex2d(-130, 120);//right window
        gl.glVertex2d(-130, 80);//right window
        
        gl.glVertex2d(-110, 120);//right window
        gl.glVertex2d(-110, 80);//right window
        
        gl.glEnd();
        
 
        gl.glBegin(GL2.GL_POINTS); 
        gl.glColor3d(1, 0, 0);
        gl.glPointSize(140.0f);
        gl.glVertex2d(-170, 70);
   
        gl.glEnd();
    }

    public void reshape(GLAutoDrawable drawable, int x, int y, int width, int height) {
    }

    public void displayChanged(GLAutoDrawable drawable, boolean modeChanged, boolean deviceChanged) {
    }

    public void dispose(GLAutoDrawable arg0) {

    }

}
