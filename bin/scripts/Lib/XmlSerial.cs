using System.Collections.Generic;
using System.IO;
using System.Xml;
using System.Xml.Serialization;

/// <summary> Helper Code to Convert Class's into a block of XML / Back into a Class. </summary>
public class XmlSerial<T>
{

    /// <summary> Convert a single Class (of customtype) into an XML String </summary>
    public static string Serialize(T input, XmlSerializerNamespaces ns = null, 
            XmlWriterSettings settings = null)
    {
        if (ns == null) ns = new XmlSerializerNamespaces();
        if (settings == null) settings = new XmlWriterSettings {Indent = true};
        var sr = new StringWriter();
        var oXs = new XmlSerializer(typeof(T));
        XmlWriter xmlwrite = XmlWriter.Create(sr, settings);
        oXs.Serialize(xmlwrite, input, ns);
        string ret = sr.ToString();
        sr.Close();
        return ret;
    }

    /// <summary> Convert a List Class's (of customtype) into an XML String </summary>
    public static string Serialize(List<T> inputList, XmlSerializerNamespaces ns = null,
            XmlWriterSettings settings = null)
    {
        if (ns == null) ns = new XmlSerializerNamespaces();
        if (settings == null) settings = new XmlWriterSettings {Indent = true};
        var sr = new StringWriter();
        var oXs = new XmlSerializer(typeof(List<T>));
        XmlWriter xmlwrite = XmlWriter.Create(sr, settings);
        oXs.Serialize(xmlwrite, inputList, ns);
        string ret = sr.ToString();
        sr.Close();
        return ret;
    }

    /// <summary>
    /// Convert an XML file into a single Class (of customtype)
    /// note singleinstance is just here as a way of telling apart the below 2 functions
    /// </summary>
    public static T Deserialize(string input) {
        var sr = new StringReader(input);
        var oXs = new XmlSerializer(typeof(T));
        var retvalue = (T)oXs.Deserialize(sr);
        sr.Close();
        return retvalue;
    }

    /// <summary> Convert an XML file into a list of Class's (of customtype) </summary>
    public static List<T> Deserialize_List(string inputList) {
        var sr = new StringReader(inputList);
        var oXs = new XmlSerializer(typeof(T));
        var retvalue = (List<T>)oXs.Deserialize(sr);
        sr.Close();
        return retvalue;
    }

}
