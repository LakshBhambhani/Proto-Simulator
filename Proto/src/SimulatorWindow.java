import java.awt.Dimension;
import java.awt.Toolkit;

import javax.swing.JEditorPane;
import javax.swing.JFrame;
import javax.swing.JScrollPane;

public class SimulatorWindow {
	
	static Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();

    public static void main(String args[]) throws Exception {
        JEditorPane website = new JEditorPane("https://google.com");
        website.setEditable(false);
        JFrame frame = new JFrame("Google");
        frame.add(new JScrollPane(website));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize((int) screenSize.getWidth(), (int) screenSize.getHeight());
        frame.setVisible(true);
    }
}